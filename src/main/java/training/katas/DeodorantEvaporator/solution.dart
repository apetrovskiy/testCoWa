library training.katas.DeodorantEvaporator;

import "dart:core";
import "dart:math";

int evaporator(double content, double evap_per_day, double threshold) {
  //Your code here
  var nthDay = 0;
  var absoluthThreshold = content * threshold / 100;
  while (content > absoluthThreshold) {
    nthDay += 1;
    content *= (100 - evap_per_day) / 100;
  }
  return nthDay;
}
