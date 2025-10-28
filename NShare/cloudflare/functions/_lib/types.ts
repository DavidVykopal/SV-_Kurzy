export interface Env {
  FILES: R2Bucket;
  AUTH_USER?: string;
  AUTH_PASS?: string;
  AUTH_TOKEN?: string;
  ALLOW_UPLOAD?: string;
  MAX_UPLOAD_SIZE?: string;
}

export interface FileEntry {
  name: string;
  path: string;
  isDir: boolean;
  size: number;
  sizeDisplay: string;
}

export interface ListResult {
  path: string;
  items: FileEntry[];
}
