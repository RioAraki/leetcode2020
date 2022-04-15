class MyHashSet {
    /** Initialize your data structure here. */
    ArrayList[] hashContainer;
    public MyHashSet() {
        hashContainer = new ArrayList[100];
        for (int i = 0; i < hashContainer.length; i++) {
            hashContainer[i] = new ArrayList<Integer>();
        }
    }

    public void add(int key) {
        int keySlot = key % 100;
        if (!hashContainer[keySlot].contains(key)) {
            hashContainer[keySlot].add(key);
        }
    }

    public void remove(int key) {
        int keySlot = key % 100;
        if (hashContainer[keySlot].contains(key)) {
            hashContainer[keySlot].remove(Integer.valueOf(key));
        }
    }

    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        int keySlot = key % 100;
        return hashContainer[keySlot].contains(Integer.valueOf(key));
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */