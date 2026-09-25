# OSI;ART
The system is built on the **OSI;ART Architecture**, physically separating the *Reactive edge* from the *Analytical Mainframe*.
To pass raw unstructured data across this gap without corrupting relies on the **ERF Protocol** to *route and filter the data.*

## What is the OSI;ART?
THE OPEN SYSTEM INTERCONNECTION; ANALYTICAL-REACTIVE TOPOLOGY, OR THE OSI:ART is the blueprint. This defines the *where* the nodes 
sit—your *Computer-lab* as the **REACTIVE NODE**, and the *Mainframe-lab* is the **ANALYTICAL MIND**

## What is the ERF?
THE **EMGRAMMIC ROUTING FRAMEWORK OR THE ERF**, This is rules of the engagement. It dictates the *how* the unstructured,
volatile "engrams" are safely packaged, routed across the network, and scrubbed, before the Analytical node processes them.

## THE TWO COMPUTER NODES, THE ANALYTICAL NODE, & THE REACTIVE NODE
### THE ANALYTICAL NODE: CIVIL LAW.
Legal systems like the Napoleonic Code, Swiss Civil Code, and Louisiana law are statutory and top-down. 
They attempt to codify every possible scenario into a strict, written constitution. 
Judges do not create laws; they rigidly apply the predefined code.

EXAMPLE WILL BE
```cobol
01  ENGRAM-RECORD.
           05  ENGRAM-ID         PIC X(10).  *> Alphanumeric, exactly 10 chars
           05  SEVERITY-LEVEL    PIC 9(02).  *> Numeric, exactly 2 digits, zero-padded
           05  EVENT-DESC        PIC X(30).  *> Alphanumeric, exactly 30 chars
           05  REACTION-CODE     PIC X(04).  *> Alphanumeric, exactly 4 chars
```

  -  The *IT Equivalent*: This is your z/OS Mainframe. Systems like *COBOL, DB2, & RACF* (Resource Access Control Facility) operate **purely on Civil Law.**

  -  The Behavior: The mainframe does not guess, interpret, or hallucinate. It executes the exact JCL and COBOL procedures written in its "constitution." If an incoming transaction (a legal case) does not match the predefined data division (the statute), the mainframe throws an ABEND (abnormal end)—it completely rejects the case.

### THE REACTIVE NODE: COMMON LAW.
Legal systems like those in the US and UK are heuristic and bottom-up. When a novel situation occurs that isn't written in a statute, judges look at past events (case law and precedent) to figure out how to react.

  -  The IT Equivalent: This is your Home Lab Edge (running Python, heuristic algorithms, or AI models).

  -  The Behavior: The Reactive Node handles the messy, unstructured reality of the outside world. When it encounters a sudden spike in traffic or an unstructured error log (an "engram"), it uses Common Law logic. It compares the event to past data (precedent) and dynamically reacts to keep the system surviving.

### THE ERF PROTOCOL: THE SUPREME COURT.
The ERF Protocol: The Supreme Court
For OSI;ART to function, you need a mechanism that translates a Common Law ruling (a dynamic reaction at the edge) 
into a Civil Law amendment (a permanent, structured record on the mainframe).

This is what your ERF protocol does. When the Reactive Node processes an "engram" using Python (Common Law),
the ERF protocol acts as the legislative bridge. It strips away the unstructured context, formats the data 
into a strict 80-byte fixed-length record, and submits it to the mainframe.

AUDITING THE SYSTEM

``` Python
import os
import json
import glob
from datetime import datetime

# ==========================================
# OSI;ART: ENGRAM GARBAGE COLLECTOR & AUDITOR
# ==========================================
# Runs on the Reactive Node to sweep local dead-letter queues.

DLQ_DIR = "./reactive_edge_dlq/"     # The chaotic storage location
MAINFRAME_DATASET = "./inengram.dat" # The structured feed staged for z/OS JCL

def audit_and_normalize(filepath):
    """The Auditing Process: Extracts structure from a chaotic engram."""
    try:
        with open(filepath, 'r') as file:
            engram = json.loads(file.read())
            
            # Heuristic Common Law logic extracting data
            raw_id = str(engram.get("error_hash", "UNKNWN"))
            raw_sev = str(engram.get("urgency", 99))
            raw_desc = str(engram.get("message", "CORRUPTED TELEMETRY"))
            raw_rx = "ACTN" if int(raw_sev) > 50 else "LOG "
            
    except Exception:
        # If the engram is completely shattered, force a rigid baseline
        raw_id = "SHATTERED"
        raw_sev = "99"
        raw_desc = "UNREADABLE BINARY NOISE"
        raw_rx = "HALT"
        
    # Enforce the Mainframe's Civil Code (PIC alignment)
    pic_id = raw_id.ljust(10)[:10]       # PIC X(10)
    pic_sev = raw_sev.zfill(2)[:2]       # PIC 9(02)
    pic_desc = raw_desc.ljust(30)[:30]   # PIC X(30)
    pic_rx = raw_rx.ljust(4)[:4]         # PIC X(04)
    
    return f"{pic_id}{pic_sev}{pic_desc}{pic_rx}"

def run_auditing_sweep():
    print(f"--- OSI;ART AUDIT CYCLE INITIATED at {datetime.now()} ---")
    
    # Locate all unprocessed engrams in the Reactive Node's queue
    engram_files = glob.glob(os.path.join(DLQ_DIR, "*.engram"))
    
    if not engram_files:
        print("Reactive Edge is 'Clear'. No engrams found.")
        return

    # Append to the staging dataset the JCL will read
    with open(MAINFRAME_DATASET, 'a') as out_file:
        for filepath in engram_files:
            # 1. Audit (Parse and Normalize to exactly 46 bytes)
            civil_record = audit_and_normalize(filepath)
            
            # 2. Transfer (Stage for Layer 6 Translation)
            out_file.write(civil_record + "\n")
            
            # 3. Garbage Collect (Erase the raw trauma from the edge node)
            os.remove(filepath) 
            
            filename = os.path.basename(filepath)
            print(f"Cleared: {filename} -> [ {civil_record} ]")

    print(f"Cycle Complete. {len(engram_files)} engrams normalized for z/OS.")

if __name__ == "__main__":
    run_auditing_sweep()
```
The Architectural Translations
The "Engram": Any file ending in .engram. It is a raw JSON crash dump or corrupted telemetry log.

-  The "Auditing" Phase: The try/except block. It reads the chaos and uses Python's string manipulation to force it into the strict PIC clauses expected by the COBOL Data Division.

-  "Garbage Collection": The os.remove(filepath) command. By unlinking the file, the operating system reclaims those disk sectors. The chaos is permanently deleted from the edge environment.

-  The "Clear" State: When the script runs and the directory is empty, the system is temporarily "Clear"—until the edge inevitably encounters new friction and generates more logs.
