#!/usr/bin/node
exports.esrever = function (list) {
  if (!Array.isArray(list)) {
    return;
  }
  let idx = list.length - 1;
  const reverseList = [];
  while (idx >= 0) {
    reverseList.push(list[idx--]);
  }
  return (reverseList);
};
