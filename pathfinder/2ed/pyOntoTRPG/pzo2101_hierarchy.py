from owlready2 import *


def create(pzo2101: Ontology):
    with pzo2101:
        class Feat(Thing): pass
        class With_proficiency_rank(Thing): pass
        class has_feat(Feat >> Feat): class_property_type = ["some"]
        class feat_of(ObjectProperty): inverse_property = has_feat
        class trained(Feat >> With_proficiency_rank): pass
        class is_trained_by(ObjectProperty): inverse_property = trained
        class has_selectable_feat(has_feat): pass
        class selectable_feat_of(ObjectProperty): inverse_property = has_selectable_feat

        class Character_backbone_feat(Feat): pass
        class Ancestry(Character_backbone_feat): pass
        class Playable_ancestry(Ancestry): pass
        class Animal_companion(Ancestry): comment = "An animal companion is a loyal comrade who follows your orders."
        class hp(Character_backbone_feat >> int, FunctionalProperty): comment = 'hit points'
        class size(Ancestry >> str, FunctionalProperty): pass
        class speed(Ancestry >> int, FunctionalProperty): comment = "land speed in feet"
        class special_speed(Ancestry >> str, FunctionalProperty): comment = "speed different from land speed"

        class Characteristic(Thing): pass
        class Ability_score(Characteristic): pass
        class ability_boost(Character_backbone_feat >> Ability_score): pass
        class ability_flaw(Ancestry >> Ability_score): pass

        class Trait(Thing): pass
        class has_trait(Ancestry >> Trait): class_property_type = ["some"]

        class With_level(Thing): pass
        class level(With_level >> int, FunctionalProperty): pass

        class Heritage(Feat): pass
        class prereq(Feat >> Feat): pass

        class Gameclass(Character_backbone_feat): pass
        class additional_skills(Gameclass >> int, FunctionalProperty): pass
        class experted(trained): pass
        class is_experted_by(ObjectProperty): inverse_property = experted
        class Class_specialization(Feat): pass

        class Background(Character_backbone_feat): pass
        class lore_speciality(Background >> str, FunctionalProperty): pass

        class Equipment(Thing): pass

        class Art(Thing): pass
        class image(AnnotationProperty): namespace = pzo2101.get_namespace("http://schema.org/")
        class depicts(Art >> Thing): pass
        class is_depicted_by(ObjectProperty): inverse_property = depicts

        class Spellcaster_class(Gameclass): pass
        class spells_per_day(Spellcaster_class >> int, FunctionalProperty):
            comment = ("Base count of spells per day, X.\n"
                       "Spells per day: cantrips = 5,  count of n-level spells = {level <= (n-1)*2: 0; level = (2*n - "
                       "1): X - 1; level >= 2*n: X}.")

        class Animal_companion_specialization(Feat):
            comment = "Specialized animal companions are more intelligent and engage in more complex behaviors."
        class Familiar_ability(Feat): pass
        class Master_ability(Feat): pass