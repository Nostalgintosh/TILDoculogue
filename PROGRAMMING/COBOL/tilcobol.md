# The bescis of COBOL

Make sure that you leave 7 lines blink, and on the 8th line most of the time write `INDENTIFICATION DIVISION.` on the 13th Collum.
- **NOTE:** ALL OF THE WRITING MUST BE ON Area B AND THE TWO NUMBERS MUST BE AT Area A.
```cbl






            
            IDENTIFICATION DIVISION.
            PROGRAM-ID. INTEFER-EXAMPLE.

            DATA DIVISION.
            WORKING-STORAGE SECTION.
        01  WS-NUMBER        PIC 9(4) VALUE 0.

            PROCEDURE DIVISION.
                MOVE 42 TO WS-NUMBER
                DISPLAY "The number is: " WS-NUMBER
                STOP RUN.
```
