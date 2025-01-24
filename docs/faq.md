```
(Get-Content -Path 'yourfile.txt' -Raw) -replace "`r`n", "`n" | Set-Content -Path poetry.lock
```

use this anytime you run a poetry command that updates something on windows. I have not found an automated way to handle this smoothly :/
