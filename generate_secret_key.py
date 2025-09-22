#!/usr/bin/env python3
"""
Script untuk generate secret key untuk production
"""

import secrets
import string

def generate_secret_key():
    """Generate secure secret key"""
    # Generate 32-byte random key
    secret_key = secrets.token_hex(32)
    return secret_key

def generate_alternative_key():
    """Generate alternative secret key"""
    # Generate using string characters
    characters = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(characters) for _ in range(64))
    return secret_key

if __name__ == '__main__':
    print("=" * 50)
    print("  Generate Secret Key for Production")
    print("=" * 50)
    print()
    
    # Generate primary secret key
    primary_key = generate_secret_key()
    print("🔑 Primary Secret Key (Recommended):")
    print(f"   {primary_key}")
    print()
    
    # Generate alternative secret key
    alternative_key = generate_alternative_key()
    print("🔑 Alternative Secret Key:")
    print(f"   {alternative_key}")
    print()
    
    print("📋 How to use:")
    print("   1. Copy one of the keys above")
    print("   2. Go to Railway Dashboard")
    print("   3. Go to Variables tab")
    print("   4. Add SECRET_KEY variable")
    print("   5. Paste the key as value")
    print("   6. Save and redeploy")
    print()
    
    print("⚠️  Important:")
    print("   - Keep this key secret")
    print("   - Don't commit to git")
    print("   - Use different key for each environment")
    print()
    
    print("=" * 50)
