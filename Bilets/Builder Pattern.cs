using System.Runtime.CompilerServices;
using System.IO;
using System.Globalization;
using System.Text;

class Program
{
    public static void Main()

    {
        string path = @"Moonlight Greatesword descr.txt";
        string name = "Moonlight Greatesword";
        string description = File.ReadAllText(path);
        Dictionary<string, int> damage = new Dictionary<string, int>() 
        {
            { "Physical Damage", 69 },
            { "Magic Damage", 130},
            { "Critical Attack", 100 }
        };
        bool effects = false;
        var MoonlightGreatesword = new TwoHandedSword()
            .SetName(name)
            .SetDamage(damage)
            .SetDescription(description)
            .SetApplyEffects(effects)
            .GetMeleeWeapon();
        Console.WriteLine(MoonlightGreatesword.ToString());
        


    }
}
class MeleeWeapon
{
    public string Type { get; set; }
    public String Name { get; set; }
    public string Description { get; set; }
    public Dictionary<string, int> Damage { get; set; }
    public bool ApplyEffects { get; set; }
    public override string ToString()
    {
        var sb = new StringBuilder();
        sb.AppendLine($"Type: {Type}" + '\n');
        sb.AppendLine($"Name: {Name}" + '\n');
        sb.AppendLine("__________________________________" + '\n');
        sb.AppendLine("Description:" + '\n' + Description);
        sb.AppendLine("__________________________________" + '\n');

        foreach (var el in Damage)
        {
            sb.AppendLine(el.Key.ToString() + ": " + el.Value.ToString());
        }

        if (ApplyEffects) 
        {
            sb.AppendLine('\n' + "Сan be tempered or resin applied" + '\n');
        }
        else
        {
            sb.AppendLine('\n' + "not possible to harden or apply resin" + '\n');
        }
        return sb.ToString();
    }
}

interface IMeleeWeaponBuilder
{
    IMeleeWeaponBuilder SetType();
    IMeleeWeaponBuilder SetName(string name);
    IMeleeWeaponBuilder SetDescription(string description);
    IMeleeWeaponBuilder SetDamage(Dictionary<string, int> damage);
    IMeleeWeaponBuilder SetApplyEffects(bool aply);
    MeleeWeapon GetMeleeWeapon();
}

class TwoHandedSword : IMeleeWeaponBuilder
{
    private MeleeWeapon _TwoHandedSword = new MeleeWeapon();
    public IMeleeWeaponBuilder SetType()
    {
        _TwoHandedSword.Type = "Two-Handed Sword";
        return this;
    }
    public IMeleeWeaponBuilder SetName(string name) 
    {
        _TwoHandedSword.Name = name;
        return this;
    }
    public IMeleeWeaponBuilder SetDescription(string description) 
    { _TwoHandedSword.Description = description; 
        return this;
    }
    public IMeleeWeaponBuilder SetDamage(Dictionary<string, int> damage)
    {
        _TwoHandedSword.Damage = damage;
        return this;
    }
    public IMeleeWeaponBuilder SetApplyEffects(bool aply)
    {
        _TwoHandedSword.ApplyEffects =  aply; 
        return this;
    }

    public MeleeWeapon GetMeleeWeapon() 
    {
        SetType();
        return _TwoHandedSword; 
    }
}
