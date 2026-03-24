import os 

def generate_invitations(template, attendees);
    if not isinstance(template, str):
        print(f"Erreur : Type invalide pour la template. Attendu : str, reçu : {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict))
    print("Erreur : Type invalide pour attendees. Attendu : une liste de dictionnaires.")
    return

    if not template.strip():
        print("Template is empty, output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        processed_content = template

        placeholders = ["name", "event_title", "event_date", "event_location"]

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            processed_content = processed_content.replace(f"{{{key}}}", str(value))
        
        filename = f"output_{index}.txt"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(processed_content)
        except Exception as e:
            print(f"Une erreur est survenue lors de l'écriture de {filename} : {e}")