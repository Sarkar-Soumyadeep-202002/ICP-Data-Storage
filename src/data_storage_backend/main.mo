import HashMap "mo:base/HashMap";

actor dataStorage {

    var store: HashMap.HashMap<Text, Text> = HashMap.HashMap<Text, Text>();

    // Function to store a key value pair in the HashMap
    public func insert(key: Text, value: Text) : async () {
        store.insert(key, value);
    }

    // Function to retreive a value with it's key
    public query func fetch(key: Text) : async ?Text {
        return store.get(key);
    }
    
    //Function to remove this value with this key
    public func remove(key: Text) : async () {
        store.remove(key);
    }
};