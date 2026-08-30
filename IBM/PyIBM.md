This Codecademy section is about **changing the normal flow of a loop**. You already know that a loop normally processes every iteration in order; `pass`, `break`, and `continue` let you alter what happens inside that repetition.

A compact mental model is:

```text
pass      → do nothing here
continue  → skip the rest of this iteration
break     → stop the entire loop
```

*Python Crash Course* covers `break` and `continue` in Chapter 7 alongside `while` loops and avoiding infinite loops. 

## `pass`

Codecademy uses:

```python
names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

for name in names:
    if 'j' in name.lower():
        pass
    else:
        print(name)
```

Here:

```python
pass
```

literally means:

> Do nothing.

So when Python reaches `"Joyce"`:

```python
'j' in 'joyce'
```

is `True`, Python executes:

```python
pass
```

which performs no action.

Then that iteration ends naturally and the loop moves to the next name.

Output:

```text
Hannah
Manny
Ezekiel
```

### Important nuance

`pass` does **not itself mean “skip this item.”**

It simply means:

> There must be a syntactically valid statement here, but I don't want it to do anything.

For example:

```python
if condition:
    pass

print("Still running")
```

`print()` will still execute afterward.

That makes `pass` useful as a placeholder while you're building code:

```python
def check_job():
    pass
```

Python accepts the function even though you haven't implemented it yet.

---

# `break`

`break` is much stronger.

```python
names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

for name in names:
    if 'h' in name.lower():
        break
    else:
        print(name)
```

Trace it:

```text
Joyce
'h' in 'joyce' → False
print Joyce

Hannah
'h' in 'hannah' → True
break
```

At that point, the **entire loop terminates**.

Python never reaches:

```text
Manny
Manoj
Ezekiel
```

So output is:

```text
Joyce
```

Think:

```text
break = EXIT LOOP NOW
```

---

# `continue`

`continue` does not terminate the loop.

It means:

> Stop processing the current iteration and immediately move to the next one.

Codecademy's example:

```python
names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

for name in names:
    if 'm' in name.lower():
        continue
    else:
        print(name)
```

For `"Manny"`:

```python
'm' in 'manny'
```

is `True`.

Python encounters:

```python
continue
```

and jumps directly to the next item.

The same happens with `"Manoj"`.

Output:

```text
Joyce
Hannah
Ezekiel
```

---

# The difference between `pass` and `continue`

This is the part worth understanding carefully.

Consider:

```python
for number in range(3):
    if number == 1:
        pass

    print(number)
```

Output:

```text
0
1
2
```

Why is `1` printed?

Because `pass` did nothing, and Python continued executing the rest of the loop body.

Now change it to:

```python
for number in range(3):
    if number == 1:
        continue

    print(number)
```

Output:

```text
0
2
```

Because when `number == 1`:

```python
continue
```

skips:

```python
print(number)
```

for that iteration.

That is the clearest comparison:

```text
pass
 │
 └── keep executing below

continue
 │
 └── jump to next iteration
```

---

# Apply this to IBM Z-style thinking

Suppose you're processing simulated job return codes:

```python
return_codes = [0, 0, 4, 8, 0]

for rc in return_codes:
    if rc == 0:
        continue

    print("Review return code:", rc)
```

Output:

```text
Review return code: 4
Review return code: 8
```

Read this as:

> For each return code, ignore normal `0` results and only process the ones needing attention.

That's a natural use for `continue`.

---

## `break` in an operations-style example

Suppose you're searching for the first serious error:

```python
return_codes = [0, 0, 4, 8, 12]

for rc in return_codes:
    if rc >= 8:
        print("Serious condition found:", rc)
        break
```

Output:

```text
Serious condition found: 8
```

Python stops once it finds the first match.

Conceptually:

```text
0  → keep going
0  → keep going
4  → keep going
8  → found it → BREAK
12 → never examined
```

---

# `pass` as a development placeholder

For your future USS automation work, you might sketch a program before implementing everything:

```python
def check_jobs():
    pass


def check_datasets():
    pass


def main():
    check_jobs()
    check_datasets()


if __name__ == "__main__":
    main()
```

This program is syntactically valid even though those functions aren't implemented yet.

That's one of the most common legitimate uses of `pass`.

---

# How these relate to CODE1

IBM CODE1 concentrates on the basic loop model—especially `while` in `marbles.py`—where a block repeats as long as a condition remains true. 

Codecademy is now adding finer control over that repeated execution:

```text
NORMAL LOOP
    ↓
process item
    ↓
process next item


continue
    ↓
skip current remainder
    ↓
next item


break
    ↓
terminate loop completely


pass
    ↓
do nothing
    ↓
continue normal execution
```

The most important thing to memorize is therefore:

```python
pass      # Do nothing.
continue  # Skip to the next iteration.
break     # Exit the loop entirely.
```

Of the three, **`continue` and `break` directly control loop execution; `pass` is essentially a no-op statement that is often useful as a placeholder.**
