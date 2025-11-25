using System.Dynamic;
/// <summary>
/// Well, I recently rewatched Dark Souls 3 once again, so 
/// it seemed interesting to me to implement a factory  
/// pattern for adding enemies to one of the locations in this game.
/// </summary>
public class Dark_Souls
{
    // here is the entry point to the program with the Main method being executed
    public static void Main()
    {
        Anor_Londo anor_Londo = Anor_Londo.GetInstance();
        anor_Londo.PopulateLocation();
        anor_Londo.DisplayEnemies();
    }
}
class Anor_Londo
///Here we are implementing a class that defines our location,
///by the way, since there cannot be two identical Locations in the game,
///I used the singleton pattern.
{
    public string Name = "Anor Londo";
    private static Anor_Londo instance;
    private Anor_Londo() {}
    public static Anor_Londo GetInstance()
    {
        if (instance == null) instance = new Anor_Londo();
        return instance;
    }
    public List<IEnemy> Enemies = new List<IEnemy>();
    //This is a list of enemies in the location
    public void PopulateLocation()
    {
        Enemies.AddRange(EnemyFactory.GroupCreate(EnemyFactory.EnemyType.SilverKnight, 3));
        Enemies.AddRange(EnemyFactory.GroupCreate(EnemyFactory.EnemyType.DeaconOfTheDepths, 7));
        Enemies.AddRange(EnemyFactory.GroupCreate(EnemyFactory.EnemyType.Slime, 10));
    }
    public void DisplayEnemies()
    //This is a method that outputs to the console a list of all enemies in a location, the value of their hp and stamina
    {
        Console.WriteLine(Name);
        foreach (var enemy in Enemies)
        {
            Console.WriteLine($"- {enemy.Name} (HP: {enemy.HP}, Stamina: {enemy.Stamina})");
        }
    }
}
public interface IEnemy
{
    /// <summary>
    /// This is the interface through which the factory that creates enemies is later implemented
    /// it stores common properties and methods for classes of enemies
    /// </summary>
    string Name { get; }
    int HP { get; }
    int Stamina { get; }
    List<string> Equipment { get; }
    void Attack(int Stamina);
    void Def(int Stamina);
}
class SilverKnight : IEnemy
{
    public string Name { get; } = "Silver Knight";
    public int HP { get; private set; } = 1050;  // Добавляем private set
    public int Stamina { get; private set; } = 140;
    public List<string> Equipment { get; } = ["The Silver Knight's sword", "The shield of the Silver Knight"];

    public void Attack(int staminaCost)
    {
        if (Stamina >= staminaCost)
            Stamina -= staminaCost;
    }

    public void Def(int staminaCost)
    {
        if (Stamina >= staminaCost)
            Stamina -= staminaCost;
    }
}

class DeaconOfTheDepths : IEnemy
{
    public string Name { get; } = "Deacon Of The Depths";
    public int HP { get; private set; } = 890;
    public int Stamina { get; private set; } = 170;
    public List<string> Equipment { get; } = ["Deacon's staff", "Kratos's dagger"];

    public void Attack(int staminaCost)
    {
        if (Stamina >= staminaCost)
            Stamina -= staminaCost;
    }

    // Дополнительный метод (не в интерфейсе)
    public void MagicAttack(int staminaCost)
    {
        if (Stamina >= staminaCost)
            Stamina -= staminaCost;
    }

    public void Def(int staminaCost)
    {
        if (Stamina >= staminaCost)
            Stamina -= staminaCost;
    }
}

class Slime : IEnemy
{
    public string Name { get; } = "Slime";
    public int HP { get; private set; } = 980;
    public int Stamina { get; private set; } = 100;
    public List<string> Equipment { get; } = [];

    public void Attack(int staminaCost)
    {
        if (Stamina >= staminaCost)
            Stamina -= staminaCost;
    }

    public void Def(int staminaCost)
    {
    }
}

public static class EnemyFactory
{
    /// <summary>
    /// This is a class that directly implements the factory 
    /// pattern, it contains a field that stores a list of available classes to create
    /// as well as two methods for single and group creation of objects of the required class
    /// </summary>
    public enum EnemyType
    {
        SilverKnight,
        DeaconOfTheDepths,
        Slime
    }

    public static IEnemy CreateEnemy(EnemyType type)    
    {
        return type switch
        {
            EnemyType.SilverKnight => new SilverKnight(),
            EnemyType.DeaconOfTheDepths => new DeaconOfTheDepths(),
            EnemyType.Slime => new Slime()
        };
    }
    public static List<IEnemy> GroupCreate(EnemyType type, int count)
    {
        var Enemies = new List<IEnemy>(count);
        for (int i = 0; i < count; i++)
        {
            Enemies.Add(CreateEnemy(type));
        }
        return Enemies;
    }
}
