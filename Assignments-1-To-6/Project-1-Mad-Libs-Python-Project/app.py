def get_superhero_inputs():
    """
    Collect inputs from the user for the superhero story.
    """
    hero_alias = input("Enter A Superhero Alias (e.g., Batman, Wonder Woman): ")
    hero_adjective = input("Enter An Adjective To Describe The Hero (e.g., brave, clever): ")
    city = input("Enter A City Name (e.g., Gotham, Metropolis): ")
    city_adjective = input("Enter An Adjective To Describe The City (e.g., dark, futuristic): ")
    villain = input("Enter A Villain's Name (e.g., Joker, Lex Luthor): ")
    power_source = input("Enter An Object That Gives The Hero Power (e.g., a magic ring, a spider bite): ")
    action_verb = input("Enter An Action Verb (e.g., flies, runs): ")
    villain_weapon = input("Enter The Villain's Weapon Or Tool (e.g., a freeze ray, a mind control device): ")
    sound_effect = input("Enter A Sound Effect (e.g., Pow!, Bam!): ")
    superpower = input("Enter A SuperPower (e.g., super strength, invisibility): ")
    return {
        "hero alias": hero_alias,
        "hero_adjective": hero_adjective,
        "city": city,
        "city_adjective": city_adjective,
        "villain": villain,
        "power_source": power_source,
        "action_verb": action_verb,
        "villain_weapon": villain_weapon,
        "sound_effect": sound_effect,
        "superpower": superpower
    }

def generate_superhero_story(inputs):
    """
    Generate the superhero origin story using the provided inputs.
    """
    story = f"""
    Once upon a time, in the {inputs['city_adjective']} city of {inputs['city']}, there lived a {inputs['hero_adjective']} hero known as {inputs['hero alias']}. One fateful day, after being exposed to {inputs['power_source']}, {inputs['hero alias']} discovered they had gained the power of {inputs['superpower']}!

    Meanwhile, the Notorious {inputs['villain']} was Wreaking Havoc in {inputs['city']} with their {inputs['villain_weapon']}. Determined to stop the Chaos, {inputs['hero alias']} decided to confront {inputs['villain']}.

    Using their {inputs['superpower']}, {inputs['hero alias']} {inputs['action_verb']} towards {inputs['villain']}. The Battle was Intense, but with a Mighty {inputs['sound_effect']}, {inputs['hero alias']} Emerged Victorious, Saving {inputs['city']} from Destruction.

    From that day forward, {inputs['hero alias']} became the Guardian of {inputs['city']}, always ready to protect the city with their incredible {inputs['superpower']}.

    """
    return story

if __name__ == "__main__":
    print("Welcome To The SuperHero Origin Story Generator!")

    play_again = True
    while play_again:
        inputs = get_superhero_inputs()
        story = generate_superhero_story(inputs)
        print("\n✨ Your SuperHero Origin Story ✨\n")
        print(story)

        # Saving feature
        save_choice = input("Would You Like To Save Your Story? (yes/no): ").lower()
        if save_choice == 'yes':
            filename = input("Enter A Filename To Save Your Story (e.g., my_story.txt): ")
            with open(filename, 'w') as file:
                file.write(story)

        # Play again feature
        play_again_choice = input("Do You Want To Play Again? (yes/no): ").lower()
        if play_again_choice != 'yes':
            play_again = False
