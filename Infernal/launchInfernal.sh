#!/bin/bash

generate_random_chars() {
    cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w "$1" | head -n 1
}

spinner() {
    local pid=$1
    local delay=0.1
    local spinstr='|/-\'
    while ps -p "$pid" > /dev/null; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

simulate_progress() {
    local duration="$1"
    local progress=0
    while ((progress < duration)); do
        sleep 0.1
        ((progress++))
        printf "Launch in progress: %s%%\r" "$((progress * 100 / duration))"
    done
    printf "Launch complete!\n"
}

main() {
    clear
    random_chars=$(generate_random_chars 8)
    spinner_pid=$$
    spinner "$spinner_pid" &
    spinner_pid=$!
    simulate_progress 5
    gnome-terminal -- python3 source/infernal.py
}

main
