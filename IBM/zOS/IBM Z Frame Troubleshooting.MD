# IBM Z Xplore JCL1 Troubleshooting Notes

These notes document the problems encountered while completing the IBM Z
Xplore JCL1 lab with user ID `Z00000`, why they happened, and the safe order
for correcting and validating the work.

## Key naming concepts

- `ZXP.PUBLIC.JCL` is the shared, read-only public JCL data set.
- `Z00000.JCL` is the personal, editable JCL data set.
- `Z00000.JCL(JCL2)` means member `JCL2` inside the personal JCL data set.
- `Z00000.OUTPUT(NAMES)` means member `NAMES` inside the personal `OUTPUT`
  partitioned data set.
- `Z00000.JCL3OUT` is a separate top-level sequential data set. It is not a
  member of `Z000000.OUTPUT`.
- In JCL, `&SYSUID.` expands to the signed-in user ID. Therefore,
  `&SYSUID..JCL3OUT` becomes `Z00000.JCL3OUT`.

## What happened and why

### 1. `Z00000.OUTPUT(NAMES) member not found`

The corrected `JCL2` job had not successfully created the `NAMES` member.
The COBOL program assigns its output file to DD name `COMBINED`, but the
provided JCL used `COMBINE` without the final `D`.

Incorrect:

```jcl
//COMBINE  DD DSN=&SYSUID..OUTPUT(NAMES),DISP=SHR
```

Correct:

```jcl
//COMBINED DD DSN=&SYSUID..OUTPUT(NAMES),DISP=SHR
```

The fix must be saved in the personal member `Z00000.JCL(JCL2)`. Submitting
the public member or an unsaved editor copy does not run the personal change.
Do not create `NAMES` manually; the successful COBOL run creates and
populates it.

### 2. `Z00000.JCL3OUT Data set not found`

`JCL3OUT` is created by the personal `JCL3` job. This message appeared because
the validator was run before a successful `Z00000.JCL(JCL3)` execution had
created the sequential data set.

### 3. `JCL3OUT contains duplicates or is missing expected single records`

The supplied `JCL3` contains deliberate duplicate input records for the lab.
The personal member initially contained both of these problems:

- Cortlandt was produced twice.
- The `BEACON` in-stream input contained two identical `Beacon - 59mi` lines.

The finished source must contain exactly one record for each station:

```text
Poughkeepsie - 74mi
New Hamburg - 65mi
Beacon - 59mi
Cold Spring - 52mi
Garrison - 50mi
Peekskill - 41mi
Cortlandt - 38mi
Croton-Harmon - 33mi
Harlem - 125th Street - 4mi
Grand Central Terminal - 0mi
```

The complete `JCL3OUT` result must have 23 records: four header records, ten
unique station records, and nine footer/information records.

### 4. `JCL ERROR` after correcting the duplicates

The first `JCL3` output allocation uses:

```jcl
DISP=(NEW,PASS,DELETE)
```

`NEW` requires `Z00000.JCL3OUT` not to exist. Resubmitting `JCL3` while the
previous `JCL3OUT` still exists causes a JCL allocation error, commonly
reported with an `IGD17001I DUPLICATE DATA SET NAME` message.

Before every `JCL3` resubmission, delete only this generated data set:

```text
Z00000.JCL3OUT
```

Do not delete `Z00000.JCL` or `Z00000.OUTPUT`.

## Correct recovery and validation order

1. Work only in the personal members under `Z00000.JCL`.
2. Save `Z00000.JCL(JCL2)` with DD name `COMBINED`.
3. Submit the personal `JCL2` and wait for `CC 0000`.
4. Confirm that `Z00000.OUTPUT(NAMES)` exists.
5. In personal `JCL3`, keep exactly one Beacon and one Cortlandt record.
6. Save `Z00000.JCL(JCL3)`.
7. If `Z00000.JCL3OUT` already exists, delete that generated data set.
8. Submit the personal `JCL3` once and wait for `CC 0000`.
9. Confirm that `Z00000.JCL3OUT` contains exactly 23 records.
10. Submit a new `ZXP.PUBLIC.JCL(CHKJCL1)` validation job.
11. Use the newest validation job result; old job output never updates.

## Do

- Confirm the editor breadcrumb begins with `/zosmf/Z000000.JCL/` before
  editing or submitting a personal member.
- Save changes before submitting.
- Check the newest job ID and its final status.
- Wait for `CC 0000` before running the validator.
- Delete the generated `Z00000.JCL3OUT` before rerunning `JCL3`.
- Submit a new `CHKJCL1` after every corrected run.

## Do not

- Do not edit or try to save `ZXP.PUBLIC.JCL`; it is read-only.
- Do not submit the public `JCL2` or `JCL3` when testing personal edits.
- Do not create `OUTPUT(NAMES)` manually.
- Do not look for `JCL3OUT` inside `Z00000.OUTPUT`.
- Do not rerun `JCL3` while an old `Z00000.JCL3OUT` exists.
- Do not delete `Z00000.JCL` or `Z00000.OUTPUT` while cleaning up JCL3 output.
- Do not rely on an old validator result after changing and rerunning a job.

## Quick error map

| Message | Meaning | Correct action |
| --- | --- | --- |
| `OUTPUT(NAMES) member not found` | Corrected personal `JCL2` did not create the member | Fix `COMBINE` to `COMBINED`, save, and submit personal `JCL2` |
| `JCL3OUT Data set not found` | Personal `JCL3` has not successfully created its output | Submit personal `JCL3` and require `CC 0000` |
| `JCL3OUT contains duplicates...` | Station records are duplicated/missing, or stale output was validated | Keep ten unique stations, rebuild `JCL3OUT`, and run a new validator |
| `JCL ERROR` from `JCL3` | `JCL3OUT` probably existed while `DISP=NEW` requested creation | Delete only `Z00000.JCL3OUT`, then submit personal `JCL3` once |

