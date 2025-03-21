"""
Memory Manager for AI Lead Magnet Platform

This module implements a simple memory management system for storing and retrieving
context across different agents in the AI Lead Magnet Platform.
"""

import os
import json
import time
from typing import Dict, Any, Optional, List
from datetime import datetime

class MemoryManager:
    """
    Memory Manager for storing and retrieving context across agents.
    
    This class provides a simple key-value storage system with persistence
    to enable agents to share information and maintain context throughout
    the lead magnet creation process.
    """
    
    def __init__(self, storage_dir: str = "./memory"):
        """
        Initialize the Memory Manager.
        
        Args:
            storage_dir: Directory to store memory files
        """
        self.storage_dir = storage_dir
        self.memory_cache = {}
        self.session_id = f"session_{int(time.time())}"
        
        # Create storage directory if it doesn't exist
        os.makedirs(storage_dir, exist_ok=True)
        os.makedirs(os.path.join(storage_dir, self.session_id), exist_ok=True)
        
        # Initialize session log
        self.session_log = []
        self._log_event("session_created", "Memory Manager initialized")
    
    def store(self, key: str, value: Any) -> None:
        """
        Store a value in memory.
        
        Args:
            key: Key to store the value under
            value: Value to store
        """
        self.memory_cache[key] = value
        
        # Persist to disk
        self._save_to_disk(key, value)
        
        # Log the event
        self._log_event("store", f"Stored value for key: {key}")
    
    def retrieve(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a value from memory.
        
        Args:
            key: Key to retrieve
            default: Default value to return if key doesn't exist
            
        Returns:
            The stored value or default if not found
        """
        # Check cache first
        if key in self.memory_cache:
            self._log_event("retrieve", f"Retrieved value for key from cache: {key}")
            return self.memory_cache[key]
        
        # Try to load from disk
        value = self._load_from_disk(key)
        if value is not None:
            # Update cache
            self.memory_cache[key] = value
            self._log_event("retrieve", f"Retrieved value for key from disk: {key}")
            return value
        
        self._log_event("retrieve", f"Key not found, returning default: {key}")
        return default
    
    def list_keys(self) -> List[str]:
        """
        List all keys in memory.
        
        Returns:
            List of keys
        """
        # Combine keys from cache and disk
        keys_from_disk = self._list_keys_from_disk()
        all_keys = list(set(list(self.memory_cache.keys()) + keys_from_disk))
        
        self._log_event("list_keys", f"Listed {len(all_keys)} keys")
        return all_keys
    
    def delete(self, key: str) -> bool:
        """
        Delete a key from memory.
        
        Args:
            key: Key to delete
            
        Returns:
            True if key was deleted, False if key didn't exist
        """
        deleted = False
        
        # Remove from cache
        if key in self.memory_cache:
            del self.memory_cache[key]
            deleted = True
        
        # Remove from disk
        file_path = os.path.join(self.storage_dir, self.session_id, f"{key}.json")
        if os.path.exists(file_path):
            os.remove(file_path)
            deleted = True
        
        if deleted:
            self._log_event("delete", f"Deleted key: {key}")
        else:
            self._log_event("delete", f"Key not found for deletion: {key}")
        
        return deleted
    
    def clear(self) -> None:
        """
        Clear all memory.
        """
        # Clear cache
        self.memory_cache = {}
        
        # Clear disk storage
        for file_name in os.listdir(os.path.join(self.storage_dir, self.session_id)):
            if file_name.endswith(".json"):
                os.remove(os.path.join(self.storage_dir, self.session_id, file_name))
        
        self._log_event("clear", "Cleared all memory")
    
    def get_session_log(self) -> List[Dict[str, Any]]:
        """
        Get the session log.
        
        Returns:
            List of log events
        """
        return self.session_log
    
    def _save_to_disk(self, key: str, value: Any) -> None:
        """
        Save a value to disk.
        
        Args:
            key: Key to save under
            value: Value to save
        """
        try:
            file_path = os.path.join(self.storage_dir, self.session_id, f"{key}.json")
            with open(file_path, 'w') as f:
                json.dump({
                    "key": key,
                    "value": value,
                    "timestamp": datetime.now().isoformat()
                }, f, default=self._json_serializer)
        except Exception as e:
            print(f"Error saving to disk: {e}")
    
    def _load_from_disk(self, key: str) -> Optional[Any]:
        """
        Load a value from disk.
        
        Args:
            key: Key to load
            
        Returns:
            The loaded value or None if not found
        """
        file_path = os.path.join(self.storage_dir, self.session_id, f"{key}.json")
        if not os.path.exists(file_path):
            return None
        
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return data["value"]
        except Exception as e:
            print(f"Error loading from disk: {e}")
            return None
    
    def _list_keys_from_disk(self) -> List[str]:
        """
        List all keys stored on disk.
        
        Returns:
            List of keys
        """
        keys = []
        try:
            for file_name in os.listdir(os.path.join(self.storage_dir, self.session_id)):
                if file_name.endswith(".json"):
                    keys.append(file_name[:-5])  # Remove .json extension
        except Exception as e:
            print(f"Error listing keys from disk: {e}")
        
        return keys
    
    def _log_event(self, event_type: str, description: str) -> None:
        """
        Log an event.
        
        Args:
            event_type: Type of event
            description: Description of event
        """
        self.session_log.append({
            "timestamp": datetime.now().isoformat(),
            "type": event_type,
            "description": description
        })
    
    def _json_serializer(self, obj: Any) -> Any:
        """
        Custom JSON serializer for handling non-serializable objects.
        
        Args:
            obj: Object to serialize
            
        Returns:
            Serializable representation of the object
        """
        if isinstance(obj, (datetime,)):
            return obj.isoformat()
        
        # Handle other non-serializable types
        try:
            return str(obj)
        except:
            return "UNSERIALIZABLE_OBJECT"


# Example usage
if __name__ == "__main__":
    # Create memory manager
    memory_manager = MemoryManager(storage_dir="./memory")
    
    # Store some values
    memory_manager.store("test_key", "test_value")
    memory_manager.store("complex_key", {
        "name": "Test Business",
        "industry": "Technology",
        "data": [1, 2, 3, 4, 5]
    })
    
    # Retrieve values
    print(memory_manager.retrieve("test_key"))
    print(memory_manager.retrieve("complex_key"))
    
    # List keys
    print(memory_manager.list_keys())
    
    # Get session log
    print(memory_manager.get_session_log())
