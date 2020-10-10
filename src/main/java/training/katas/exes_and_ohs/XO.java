package training.katas.exes_and_ohs;

public class XO {

  public static boolean getXO(String str) {

    // Good Luck!!
    var lowerCasedString = str.toLowerCase();
    var x = 'x';
    var o = 'o';
    System.out.println(lowerCasedString);
    System.out.println(
        lowerCasedString.chars().filter(i -> i == x).count() == lowerCasedString.chars().filter(i -> i == o).count());
    return lowerCasedString.chars().filter(i -> i == x).count() == lowerCasedString.chars().filter(i -> i == o).count();
  }
}
