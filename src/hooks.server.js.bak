export async function handle({ event, resolve }) {
  const { pathname } = event.url;

  if (pathname === '/') {
    const supported = ['de', 'en', 'no'];
    const acceptLanguage = event.request.headers.get('accept-language');

    let lang;

    if (!acceptLanguage) {
      // Kein Header vorhanden -> wir wissen nichts über die Präferenz -> Deutsch
      lang = 'de';
    } else {
      // z.B. "en-US,en;q=0.9,de;q=0.8" -> ["en", "en", "de"]
      const preferred = acceptLanguage
        .split(',')
        .map(part => part.split(';')[0].trim().split('-')[0].toLowerCase());

      const foundSupported = preferred.find(l => supported.includes(l));

      // Browser hat eine Sprache genannt, aber keine, die wir anbieten -> Englisch
      // Browser hat gar keine auswertbare Angabe -> würde hier auch Englisch treffen,
      // ist aber durch den !acceptLanguage-Check oben schon abgefangen
      lang = foundSupported || 'en';
    }

    return new Response(null, {
      status: 302,
      headers: { location: `/${lang}/` }
    });
  }

  return resolve(event);
}