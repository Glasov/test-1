// Singleton pattern realisation 
class YabaiBeatricheF33t
{
    //Singleton assumes that class will have only one instance
    //So let`s create class that defines me, that is YabaiBeatricheF33t
    private static YabaiBeatricheF33t instance;
    //This is varable that contains an instance of the class, so it`s contains me 
    private YabaiBeatricheF33t() {}
    //Now we create class constructor 
    public static YabaiBeatricheF33t getInstaince()
    {
        if (instance == null)
        {
            instance = new YabaiBeatricheF33t();
        }
        return instance;
    }
    //So we create a method that will create and return an instance of the class, if this instance does not exist or just return already existing instance 
}
