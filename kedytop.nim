import os, strutils, terminal

# Ekranı temizle (ANSI kaçış karakteri ile)
# Clear the screen using ANSI escape code
proc clearScreen() =
  stdout.write("\x1B[2J\x1B[H")

# String sadece sayılardan mı oluşuyor kontrolü
# Check if a string contains only digits
proc isAllDigits(s: string): bool =
  for c in s:
    if not c.isDigit:
      return false
  return s.len > 0

# /proc dizininden tüm PID'leri al
# List all PIDs (numeric directories) from /proc
proc listPids(): seq[int] =
  result = @[]
  for entry in walkDir("/proc"):
    let nameStr = splitFile(entry.path).name
    if isAllDigits(nameStr):
      result.add(parseInt(nameStr))

# Belirtilen PID için komut adını döndür
# Return the command name for given PID
proc getCmd(pid: int): string =
  let cmdPath = "/proc/" & $pid & "/comm"
  if fileExists(cmdPath):
    return readFile(cmdPath).strip()
  return ""

# Ana işlem döngüsü
# Main process loop
proc main() =
  while true:
    clearScreen()
    # ASCII kedi logosu / ASCII cat logo
    echo """
     /\\_/\\  
    ( o.o )  kedyTop
     > ^ <
    """
    echo "PID     CMD"
    echo "----------------"
    let pids = listPids()
    for pid in pids[0..<min(20, pids.len)]:
      let cmd = getCmd(pid)
      echo $pid & "  " & cmd
    sleep(2000)  # 2 saniye bekle / wait 2 seconds

# Program doğrudan çalıştırıldığında main çağrılır
# If run directly, call main()
when isMainModule:
  main()