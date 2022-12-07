import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input.txt"));
        Tree root = new Tree("/", 0, null);
        Tree current = root;
        while(scanner.hasNextLine()) {
            String[] lineparts = scanner.nextLine().split(" ");
            switch(lineparts[0]) {
                case "$" -> {
                    if(lineparts[1].equals("cd")) {
                        switch (lineparts[2]) {
                            case "/" -> current = root;
                            case ".." -> current = current.parent;
                            default -> current = current.getChild(lineparts[2]);
                        }

                    }
                }
                case "dir" ->
                    current.addChild(new Tree(lineparts[1], 0, current));
                default ->
                    current.addChild(new Tree(lineparts[1], Integer.parseInt(lineparts[0]), current));
            }
        }
        root.initializeSize();
        System.out.println(root.sizesLowerThan(100000));
        int spaceNeeded = 30_000_000 - (70_000_000 - root.size);
        System.out.println(root.smallestAboveBound(spaceNeeded));


    }
    static class Tree {
        String name;
        Tree parent;
        List<Tree> children;
        int size;
        public Tree(String name, int size, Tree parent) {
            this.name = name;
            this.size = size;
            this.parent = parent;
            children = new ArrayList<>();
        }
        public void addChild(Tree tree) {
            children.add(tree);
        }
        public Tree getChild(String name) {
            for(Tree tree : children) {
                if (tree.name.equals(name))
                    return tree;
            }
            return null;
        }
        public int initializeSize() {
            if(children.size() > 0) {
                int total = 0;
                for(Tree child : children) {
                    total += child.initializeSize();
                }
                size = total;
                return total;
            }
            return size;
        }
        public int sizesLowerThan(int bound) {
            if(children.size() > 0) {
                int total = 0;
                if(this.size < bound) {
                    total += this.size;
                }
                for(Tree child : children) {
                    total += child.sizesLowerThan(bound);
                }
                return total;
            }
            return 0;
        }
        public int smallestAboveBound(int bound) {
            if(children.size() > 0){
                int smallest = Integer.MAX_VALUE;
                if(this.size > bound) {
                    smallest = this.size;
                }
                for(Tree child : children) {
                    if(child.smallestAboveBound(bound) < smallest) {
                        smallest = child.smallestAboveBound(bound);
                    }
                }
                return smallest;
            }
            return Integer.MAX_VALUE;
        }
    }
}

