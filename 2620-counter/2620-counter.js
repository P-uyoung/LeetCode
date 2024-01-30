function createCounter(n) {
  let i = 0;
  return () => n + i++;
}