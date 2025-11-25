using System;

class Program
{
    static void Main()
    {
        List<int> lst = [1,2,3,1444,23,222222,3133,0,0,0,0,1,223,555,666];
        ContextSort Sorter = new ContextSort();
        Sorter.SelectStratagy(new QuickSort());
        Sorter.sort(lst);

    }
}

interface IAlgorithm
{
    List<int> sort(List<int> list);
}

class QuickSort : IAlgorithm
{
    public List<int> sort(List<int> list)
    {
        //Здесь должна быть реализация алгоритма
        return list;
    }
}
class BubbleSort : IAlgorithm
{
    public List<int> sort(List<int> list)
    {
        //Здесь тоже должна быть реализация алгоритма 
        return list;
    }
}
class ContextSort
{
    private IAlgorithm sorter;
    public void SelectStratagy(IAlgorithm sorter)
    {
        this.sorter = sorter;
    }
    public List<int> sort(in List<int> list)
    {
        return sorter.sort(list);
    }
}