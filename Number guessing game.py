# ── GAME SETTINGS ──────────────────────────────────────────────
secret = 27      # The hidden number the player must guess
max_attempts = 5

# ── SETUP ──────────────────────────────────────────────────────
count = 0
guess = 0

print("=" * 42)
print("  ==========================================" \
"              " \
"               🎮  NUMBER GUESSING GAME" \
"" \
"        ==========================================")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

# ── MAIN GAME LOOP ─────────────────────────────────────────────
while count < max_attempts and guess != secret:

    guess = int(input("Enter your guess: "))
    count += 1

    if guess == secret:
        print(f"🎉 Congratulations! You guessed the number in {count} attempt(s).")

    else:
        # Calculate difference without abs()
        if guess > secret:
            diff = guess - secret
        else:
            diff = secret - guess

        # Give hint
        if diff >= 20:
            print("🫩 Seriouly?")
        elif diff >= 10:
            print("🥱 Come(*yawn*) on")
        elif diff >= 5:
            print("🤓 Close!")
        else:
            print("😆🤘 Alright!")

        remaining = max_attempts - count

        if remaining > 0:
            print("Lives left:", end=" ")
            for i in range(remaining):
                print("❤️", end=" ")
            print()

# ── GAME OVER CHECK ────────────────────────────────────────────
if guess != secret:
    print(f"\n💀 Game Over! The secret number was {secret}.")