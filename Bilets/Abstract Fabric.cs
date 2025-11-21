using System;
using System.Linq.Expressions;
class CharacterCreate
{
    public static void Main()
    {
        //предположим мы реализовали логику для выбора персонажа (мне немного лень это писать в 3часа ночи :))
        //допустим игрок выбрал класс Война и дал ему имя 'ALoxa665'
        WarriorCreate ALoxa665 = new WarriorCreate();
        var CharacterClass = ALoxa665.CreateCharacter();
        var EquippedWeapon = ALoxa665.CreateWeapon();
        var EquippedArmor = ALoxa665.CreateArmor();
        Console.WriteLine($"character class {CharacterClass.ClassName}");
        foreach(var stat in CharacterClass.stats())
        {
            Console.WriteLine($"{stat.Key} : {stat.Value}");
        }
        Console.WriteLine($"Equipped Armor: {EquippedArmor.ArmorName}");
        Console.WriteLine($"Equipped Weapon: {EquippedWeapon.WeaponName}");
    }
}
public interface IAbstractCharacterCreate
{
    ICharacter CreateCharacter();
    IWeapon CreateWeapon();
    IArmor CreateArmor();
}
public interface ICharacter
{
    string ClassName { get; }
    int SoulLevel { get; }
    int Vigor { get; }
    int Attunement { get; }
    int Endurance { get; }
    int Vitality { get; }
    int Strength { get; }
    int Dexterity { get; }
    int Intelligence { get; }
    int Faith { get; }
    int Luck { get; }
    Dictionary<string, int> stats();
}
public interface IWeapon
{
    string WeaponName { get; }
    int WeaponDamage { get; }
}
public interface IArmor
{
    string ArmorName { get; }
    int ArmorDef { get; }
}
class Mercenary : ICharacter
{
    public string ClassName { get; } = "Mercenary";
    public int SoulLevel { get; } = 8;
    public int Vigor { get; } = 11;
    public int Attunement { get; } = 12;
    public int Endurance { get; } = 11;
    public int Vitality { get; } = 10;
    public int Strength { get; } = 10;
    public int Dexterity { get; } = 16;
    public int Intelligence { get; } = 10;
    public int Faith { get; } = 8;
    public int Luck { get; } = 9;
    public Dictionary<string, int> stats() => new Dictionary<string, int>()
        {
            {"SoulLevel", this.SoulLevel}, {"Vigor", this.Vigor}, {"Attunement", this.Attunement},
             {"Endurance", this.Endurance}, {"Vitality", this.Vitality}, {"Strength", this.Strength},
              {"Dexterity", this.Dexterity}, {"Intelligence", this.Intelligence}, {"Faith", this.Faith},
              {"Luck", this.Luck}
        };

}
class Warrior : ICharacter
{
    public string ClassName { get; } = "Warrior";
    public int SoulLevel { get; } = 7;
    public int Vigor { get; } = 14;
    public int Attunement { get; } = 6;
    public int Endurance { get; } = 12;
    public int Vitality { get; } = 11;
    public int Strength { get; } = 16;
    public int Dexterity { get; } = 9;
    public int Intelligence { get; } = 8;
    public int Faith { get; } = 9;
    public int Luck { get; } = 11;
    public Dictionary<string, int> stats() => new Dictionary<string, int>()
        {
            {"SoulLevel", this.SoulLevel}, {"Vigor", this.Vigor}, {"Attunement", this.Attunement},
             {"Endurance", this.Endurance}, {"Vitality", this.Vitality}, {"Strength", this.Strength},
              {"Dexterity", this.Dexterity}, {"Intelligence", this.Intelligence}, {"Faith", this.Faith},
              {"Luck", this.Luck}
        };

}
class Sorcerer : ICharacter
{
    public string ClassName { get; } = "Sorcerer";
    public int SoulLevel { get; } = 6;
    public int Vigor { get; } = 9;
    public int Attunement { get; } = 16;
    public int Endurance { get; } = 9;
    public int Vitality { get; } = 7;
    public int Strength { get; } = 7;
    public int Dexterity { get; } = 12;
    public int Intelligence { get; } = 16;
    public int Faith { get; } = 7;
    public int Luck { get; } = 12;
    public Dictionary<string, int> stats() => new Dictionary<string, int>()
        {
            {"SoulLevel", this.SoulLevel}, {"Vigor", this.Vigor}, {"Attunement", this.Attunement},
             {"Endurance", this.Endurance}, {"Vitality", this.Vitality}, {"Strength", this.Strength},
              {"Dexterity", this.Dexterity}, {"Intelligence", this.Intelligence}, {"Faith", this.Faith},
              {"Luck", this.Luck}
        };
}

class The_Mercenarys_Scimitars : IWeapon
{
    public string WeaponName { get; } = "The Mercenary's Scimitars";
    public int WeaponDamage { get; } = 99;
}
class The_Axe: IWeapon
{
    public string WeaponName { get; } = "The Axe";
    public int WeaponDamage { get; } = 125;
}

class The_Wizards_Staff : IWeapon
{
    public string WeaponName { get; } = "The Wizard's Staff";
    public int WeaponDamage { get; } = 60;
}
class The_Mercenarys_Set : IArmor
{
    public string ArmorName { get; } = "The Mercenary's Set";
    public int ArmorDef { get; } = 21;

}
class The_Northern_Set : IArmor
{
    public string ArmorName { get; } = "The Northern Set";
    public int ArmorDef { get; } = 27;

}
class The_Sorcerers_Set : IArmor
{
    public string ArmorName { get; } = "The Sorcerer's Set";
    public int ArmorDef { get; } = 11;

}

class MercenaryCreate: IAbstractCharacterCreate
{
   public ICharacter CreateCharacter()
    {
        return new Mercenary();
    }
   public IWeapon CreateWeapon()
    {
        return new The_Mercenarys_Scimitars();
    }
   public IArmor CreateArmor()
    {
        return new The_Mercenarys_Set();
    }
}
class WarriorCreate : IAbstractCharacterCreate
{
    public ICharacter CreateCharacter()
    {
        return new Warrior();
    }
    public IWeapon CreateWeapon()
    {
        return new The_Axe();
    }
    public IArmor CreateArmor()
    {
        return new The_Northern_Set();
    }
}
class SorcererCreate : IAbstractCharacterCreate
{
    public ICharacter CreateCharacter()
    {
        return new Sorcerer();
    }
    public IWeapon CreateWeapon()
    {
        return new The_Wizards_Staff();
    }
    public IArmor CreateArmor()
    {
        return new The_Sorcerers_Set();
    }

}