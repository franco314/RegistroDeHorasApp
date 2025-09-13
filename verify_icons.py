#!/usr/bin/env python3
"""
Verify Android launcher icons exist and are properly sized.
"""

import os
import sys

def verify_icons():
    """Verify all launcher icons exist in the correct directories."""
    base_path = 'frontend_kotlin/app/src/main/res'
    densities = ['mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']
    expected_sizes = {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}
    icon_types = ['ic_launcher.webp', 'ic_launcher_round.webp']
    
    print("Android Launcher Icons Verification")
    print("=" * 50)
    
    all_exist = True
    total_size = 0
    
    for density in densities:
        mipmap_dir = os.path.join(base_path, f'mipmap-{density}')
        
        if not os.path.exists(mipmap_dir):
            print(f"❌ Directory missing: {mipmap_dir}")
            all_exist = False
            continue
            
        print(f"\n📁 {mipmap_dir}")
        
        for icon_type in icon_types:
            icon_path = os.path.join(mipmap_dir, icon_type)
            
            if os.path.exists(icon_path):
                file_size = os.path.getsize(icon_path)
                total_size += file_size
                size_kb = file_size / 1024
                
                # Try to get image dimensions if PIL is available
                try:
                    from PIL import Image
                    with Image.open(icon_path) as img:
                        width, height = img.size
                        expected = expected_sizes[density]
                        
                        if width == expected and height == expected:
                            print(f"  ✅ {icon_type:20} {width}x{height} ({size_kb:.1f} KB)")
                        else:
                            print(f"  ⚠️  {icon_type:20} {width}x{height} (expected {expected}x{expected}, {size_kb:.1f} KB)")
                except ImportError:
                    print(f"  ✅ {icon_type:20} exists ({size_kb:.1f} KB) - cannot verify size (PIL not available)")
                except Exception as e:
                    print(f"  ❌ {icon_type:20} error reading file: {e}")
                    all_exist = False
                    
            else:
                print(f"  ❌ {icon_type:20} MISSING")
                all_exist = False
    
    print(f"\n{'='*50}")
    print(f"Total icons size: {total_size/1024:.1f} KB")
    
    if all_exist:
        print("✅ All launcher icons are present!")
        return True
    else:
        print("❌ Some icons are missing or have issues.")
        return False

def main():
    if not os.path.exists('frontend_kotlin'):
        print("❌ Error: Not in the project root directory (frontend_kotlin not found)")
        print("Please run this script from the project root directory.")
        sys.exit(1)
    
    success = verify_icons()
    
    if not success:
        print("\n💡 To regenerate missing icons, run:")
        print("   python generate_launcher_icons.py --output frontend_kotlin/app/src/main/res")
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()