**Precondition:**

```python
0 <= len(commands) <= 20
all(re.match("\APUSH \d\Z", c) or с == "POP" or c == "PEEK" for c in commands)
```
