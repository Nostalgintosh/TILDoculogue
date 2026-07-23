





            
            IDENTIFICATION DIVISION.
            PROGRAM-ID. INTEFER-EXAMPLE.

            DATA DIVISION.
            WORKING-STORAGE SECTION.
        01  WS-NUMBER        PIC 9(4) VALUE 0.

            PROCEDURE DIVISION.
                MOVE 42 TO WS-NUMBER
                DISPLAY "The number is: " WS-NUMBER
                STOP RUN.
