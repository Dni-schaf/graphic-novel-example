import { minChapter, maxChapter } from '$lib/data/chapterConfig.js';

export function getCurrentChapterNumber(pathname) {
  const match = pathname.match(/chapter(\d+)/);
  return match ? parseInt(match[1], 10) : null;
}

export function getChapterStartUrl(lang, chapterNumber) {
  return `/${lang}/chapter${chapterNumber}#srt`;
}

export function getNextChapterUrl(lang, currentChapterNumber) {
  const next = getNextChapterNumber(currentChapterNumber);
  return next !== null ? `/${lang}/chapter${next}#srt` : null;
}

export function getPrevChapterUrl(lang, currentChapterNumber) {
  const prev = getPrevChapterNumber(currentChapterNumber);
  return prev !== null ? `/${lang}/chapter${prev}#end` : null;
}

export function getNextChapterNumber(current) {
  const next = current + 1;
  return next <= maxChapter ? next : null;
}

export function getPrevChapterNumber(current) {
  const prev = current - 1;
  return prev >= minChapter ? prev : null;
}