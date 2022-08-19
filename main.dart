DateTime date1 = DateTime.parse("2022-02-12 16:32:24");
DateTime date2 = DateTime.parse("2023-05-12 16:45:00");

String convert(DateTime date1, DateTime date2) {
  Duration diff = date1.difference(date2);

  int days = diff.inDays;
  int hours = diff.inHours % 24;
  int minutes = diff.inMinutes % 60;
  int seconds = diff.inSeconds % 60;

  return "$days jours,\n $hours heures,\n $minutes minutes & $seconds secondes";
}
