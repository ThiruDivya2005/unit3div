sorted_students = sorted(student_list,
                         key=lambda student: student.cgpa,
                         reverse=True)
return sorted_students


# Example  usage:
students = [
  student("Hari","A123",7.8),
  student("srikanth","A124",8.9),
  student("sridevi","A125",9.1),
  student("kanika","A126",9.9),
]

sorted_students = sort_students(students)
  