def forward_chaining(initial_facts, rules):

    # Store all known facts
    facts = set(initial_facts)

    # Final conclusions
    conclusions = []

    # Inference log
    logs = []

    # Rule counter
    fired_rules = set()

    step = 1

    while True:

        new_fact_added = False

        for rule in rules:

            rule_id = rule["id"]

            conditions = rule["conditions"]

            conclusion = rule["conclusion"]

            # Skip if rule already fired
            if rule_id in fired_rules:
                continue

            # Check if all conditions are satisfied
            if all(condition in facts for condition in conditions):

                fired_rules.add(rule_id)

                logs.append({
                    "step": step,
                    "rule_id": rule_id,
                    "conditions": conditions,
                    "conclusion": conclusion
                })

                step += 1

                if conclusion not in facts:

                    facts.add(conclusion)

                    conclusions.append(conclusion)

                    new_fact_added = True

        if not new_fact_added:
            break

    return {
        "facts": list(facts),
        "conclusions": conclusions,
        "logs": logs,
        "rules_fired": len(fired_rules),
        "steps": step - 1
    }