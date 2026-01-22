# Human Attention Span Monitoring Timer

taskName = input("Enter task name: ")
attentionLimit = int(input("Enter attention time limit (minutes): "))

print("\nMonitoring attention for task:", taskName)

for minute in range(1, attentionLimit + 2):
    print("Minute", minute, ": Focused")

    if minute > attentionLimit:
        print("\nAttention limit exceeded!")
        print("Recommendation: Take a short break.")
        break
