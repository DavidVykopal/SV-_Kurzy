import type { Env } from "./_lib/types";
import { isBasicAuthValid, unauthorizedResponse } from "./_lib/utils";

export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  if (isBasicAuthValid(request, env)) {
    const redirectUrl = new URL("/", request.url);
    return Response.redirect(redirectUrl.toString(), 302);
  }
  return unauthorizedResponse("Authentication required", { basic: true });
};
