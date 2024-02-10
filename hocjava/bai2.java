import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class bai2{
    public static void main(String[] args){
        Set<Integer> set = new TreeSet<Integer>();
        set.add(8);
        set.add(2);
        set.add(1);
        set.add(9);
        set.add(2);
        System.out.println(set);
    }
}