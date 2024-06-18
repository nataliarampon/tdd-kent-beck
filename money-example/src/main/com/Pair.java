package main.com;

public class Pair {
    private String to;
    private String from;

    public Pair(String from, String to) {
        this.to = to;
        this.from = from;
    }

    @Override
    public int hashCode() {
        // TODO: better hash when needed
        return 0;
    }

    @Override
    public boolean equals(Object obj) {
        Pair pair = (Pair) obj;
        return this.from.equals(pair.from) && this.to.equals(pair.to);
    }
}
