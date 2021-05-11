package training.katas.exes_and_ohs;

@SuppressWarnings("PMD")
public class XO {

  public static boolean getXO(String str) {

    // Good Luck!!
    var lowerCasedString = str.toLowerCase();
    var x = 'x';
    var o = 'o';
    return lowerCasedString.chars().filter(i -> i == x).count()
        == lowerCasedString.chars().filter(i -> i == o).count();
  }
}
