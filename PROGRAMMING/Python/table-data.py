'''
   IDENTIFICATON DIVISON.
   PROGRAM-ID. Table Data.
   AUTHER.     CODECADEMY.
'''
#  DATA DIVISION
tables = {
  1: ['Jiho', False],       # PIC 9  VALUE "Jiho is False".
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

#  PROCEDURE DIVISION.
def assign_table(table_number, name, vip_status=False): 
  tables[table_number] =  [name, vip_status]
#  PERFORM 100-ASSIGN-TABLE-TONI
assign_table(6, 'Yoni', False)
print(tables)
#  PERFORM 200-ASSIGN-TABLE-MARTHA
assign_table(table_number=3, name='Martha', vip_status=True)
print(tables)
#  PERFORM 300-TABLE-KARLA
assign_table(4, 'Karla')
print(tables)
