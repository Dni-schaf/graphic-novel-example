import { page } from '$app/state';
import { goto } from '$app/navigation';

export function switchLanguage(newLang) {
  const pathParts = page.url.pathname.split('/');
  pathParts[1] = newLang;
  goto(pathParts.join('/') + page.url.hash);
}