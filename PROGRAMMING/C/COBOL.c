//  PROCEDURE DIVISION.
int main() {
  char cust_id[11];                  /* MEMORY ALLOCATON IN DATA DIVISION */
  strcpy(cust_id, "0123456789");     // MOVE "0123456789"
  printf("ID: %s\n", cust_is);       // DISPLAY "CUSTORMER ID: "
  return 0;                          // STOP RUN.
}
/* The PROCEDURE DIVISION in COBOL is simular to  the `int main ()` function in C.
the `char cust_id[11];` is the Memory Allocation in THE DATA DIVISION to keeps it
data.
The `strcpy(cust_id, "0123456789");` is the `MOVE` Function, to MOVE the numbers-
in the print function, while the printf("ID: %s/n", cust_is); the to DISPLAY the
CUSTOMER'S ID out the respected numbers.
The `return 0;` is to STOP RUNNING by RETURN TO ZERO. tells that zero is nothing
so just STOP RUN.
*/
