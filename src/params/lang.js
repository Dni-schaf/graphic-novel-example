const supported = ['de', 'en', 'no'];

export function match(param) {
  return supported.includes(param);
}