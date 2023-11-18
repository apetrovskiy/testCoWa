package training.katas.exes_and_ohs

object ExesAndOhs {

  def xo(
      str: String
  ): Boolean = // str toLowerCase filter { i -> i == 'x' } count == str toLowerCase filter { i -> i == 'o' } count
    str.toLowerCase().chars().filter(i => i == 'x').count() == str
      .toLowerCase()
      .chars()
      .filter(i => i == 'o')
      .count()
}
