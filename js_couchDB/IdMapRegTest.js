import doc from "./fireData.js";

// couchDB好像不支持很多ES6及以上的写法
let map_fun = function (doc) {
  var pattern; // 正则表达式
  var res; // 正则结果
  // console.log(doc);
  if (doc.type === "log") {
    pattern = /\bId\b=[A-Za-z0-9]*/g;
    doc.content.forEach(function (line) {
      // console.log(line);
      // 按行遍历
      res = line.match(pattern);
      if (res) {
        console.log(res[0]);
        console.log(line);
        // emit(res[0], line);
      }
    });
  } else if (doc.type === "fireData") {
    pattern = /\bId\b:[A-Za-z0-9]*/g;
    for (var i in doc.content) {
      res = doc.content[i].match(pattern);
      if (res) {
        console.log(res);
        console.log(doc.content.join(""));
        // emit(res[0], doc.content.join(""));
        break;
      }
    }
  } else if (doc.type === "plotData") {
    pattern = /\bId\b:[A-Za-z0-9]*/g;
    doc.content.forEach(function (line) {
      res = line.match(pattern);
      if (res) {
        console.log(res);
        console.log(doc.content.join(""));
        // emit(res[0], doc.content.join(""));
      }
    });
  }
};

map_fun(doc);
