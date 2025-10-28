import type { Env, FileEntry } from "./types";
import { formatSize, listPrefixFor, normalizePath } from "./utils";

const META_PREFIX = "__meta/";

export async function listDirectory(env: Env, rawPath: string): Promise<FileEntry[]> {
  const path = normalizePath(rawPath);
  const prefix = listPrefixFor(path);
  const result = await env.FILES.list({
    prefix,
    delimiter: "/",
    include: ["customMetadata", "httpMetadata"],
    limit: 1000,
  });

  const items: FileEntry[] = [];

  for (const folder of result.delimitedPrefixes ?? []) {
    if (folder.startsWith(META_PREFIX)) continue;
    const relative = folder.slice(prefix.length).replace(/\/$/, "");
    if (!relative) continue;

    items.push({
      name: relative,
      path: path ? `${path}/${relative}` : relative,
      isDir: true,
      size: 0,
      sizeDisplay: "-",
    });
  }

  for (const object of result.objects ?? []) {
    if (object.key.startsWith(META_PREFIX)) continue;
    if (object.key === prefix) continue;
    const relative = object.key.slice(prefix.length);
    if (!relative || relative.endsWith("/")) continue;
    items.push({
      name: relative,
      path: path ? `${path}/${relative}` : relative,
      isDir: false,
      size: object.size,
      sizeDisplay: formatSize(object.size),
    });
  }

  return items.sort((a, b) => {
    if (a.isDir && !b.isDir) return -1;
    if (!a.isDir && b.isDir) return 1;
    return a.name.localeCompare(b.name, undefined, { sensitivity: "base" });
  });
}

export async function deletePath(env: Env, rawPath: string): Promise<void> {
  const path = normalizePath(rawPath);
  if (!path) throw new Error("Cannot delete root");
  if (path.startsWith(META_PREFIX)) throw new Error("Restricted path");

  const prefix = listPrefixFor(path);
  const toDelete: string[] = [];

  let cursor: string | undefined;
  do {
    const res = await env.FILES.list({ prefix, cursor, limit: 1000 });
    for (const obj of res.objects) {
      toDelete.push(obj.key);
    }
    cursor = res.truncated ? res.cursor : undefined;
  } while (cursor);

  if (toDelete.length === 0) {
    // Try deleting as single file
    await env.FILES.delete(path);
    return;
  }

  // Delete in batches of 1000
  for (let i = 0; i < toDelete.length; i += 1000) {
    const batch = toDelete.slice(i, i + 1000);
    await env.FILES.delete(batch);
  }
}
