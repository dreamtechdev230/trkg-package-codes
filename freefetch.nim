#!/usr/bin/env -S nim r
import os, osproc, strutils

proc countDirs(path: string): int =
  var count = 0
  for entry in walkDir(path):
    if entry.kind == pcDir:
      inc(count)
  return count

proc main() =
  echo """
   /\\_/\\
  ( o.o )
   > ^ <
  """

  let user = getEnv("USER", "unknown")
  let host = try:
    execProcess("hostname", options = {poUsePath}).strip()
  except OSError:
    "unknown"

  var unameInfo = "unknown"
  try:
    unameInfo = execProcess("uname -s -a", options = {poUsePath}).strip()
  except:
    discard

  var cpu = "unknown"
  if fileExists("/proc/cpuinfo"):
    for line in lines("/proc/cpuinfo"):
      if "model name" in line:
        cpu = line.split(":")[1].strip()
        break

  var uptime = "unknown"
  if fileExists("/proc/uptime"):
    let content = readFile("/proc/uptime").split()
    if content.len > 0:
      let seconds = parseFloat(content[0])
      uptime = $int(seconds / 60) & " mins"

  let de = getEnv("XDG_CURRENT_DESKTOP", "unknown")
  let wm = getEnv("DESKTOP_SESSION", "unknown")

  var pkgs = "unknown"
  if dirExists("/var/lib/pacman/local"):
    try:
      pkgs = $countDirs("/var/lib/pacman/local")
    except:
      discard

  echo "User    : ", user
  echo "Host    : ", host
  echo "Uname   : ", unameInfo
  echo "CPU     : ", cpu
  echo "DE      : ", de
  echo "WM      : ", wm
  echo "Packages: ", pkgs
  echo "Uptime  : ", uptime

when isMainModule:
  main()
