function sumBetween(f, a, b) {
  function loop(x, acc) {
    if (x > b) {
      return acc;
    } else {
      return loop(x + 1, acc + f(x));
    }
  }
  return loop(a, 0);
}

function main() {
  console.log(sumBetween(x => x, 1, 10));
}

main();
/**
 * 
 * @abstract TS代码如下
 * 
 * function sumBetween(f: (x: number) => number, a: number, b: number): number {
  function loop(x: number, acc: number): number {
    if (x > b) {
      return acc;
    } else {
      return loop(x + 1, acc + f(x));
    }
  }
  return loop(a, 0);
}

function main(): void {
  console.log(sumBetween(x => x, 1, 10));
}

main();

 */
