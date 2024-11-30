const cond = (x, y) => x < y;

const insert = (x, xs) => {
  if (xs.length === 0) {
    return [x];
  } else {
    //xs 的第一个元素赋值给 y，并将剩余的元素以数组的形式赋值给 ys。
    const [y, ...ys] = xs;
    if (cond(x, y)) {
      return [x, y, ...ys];
    } else {
      return [y, ...insert(x, ys)];
    }
  }
};

const main = () => {
  console.log(insert(4, [1, 8]));
};

main();
