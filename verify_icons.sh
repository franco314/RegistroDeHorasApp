#!/bin/bash
# Verify Android launcher icons exist

echo "Android Launcher Icons Verification"
echo "===================================================="

BASE_PATH="frontend_kotlin/app/src/main/res"
DENSITIES=("mdpi" "hdpi" "xhdpi" "xxhdpi" "xxxhdpi")
SIZES=("48x48" "72x72" "96x96" "144x144" "192x192")
ICONS=("ic_launcher.webp" "ic_launcher_round.webp")

total_size=0
all_exist=true

for i in "${!DENSITIES[@]}"; do
    density="${DENSITIES[$i]}"
    expected_size="${SIZES[$i]}"
    mipmap_dir="$BASE_PATH/mipmap-$density"
    
    echo ""
    echo "📁 $mipmap_dir"
    
    if [ ! -d "$mipmap_dir" ]; then
        echo "  ❌ Directory missing: $mipmap_dir"
        all_exist=false
        continue
    fi
    
    for icon in "${ICONS[@]}"; do
        icon_path="$mipmap_dir/$icon"
        
        if [ -f "$icon_path" ]; then
            file_size=$(stat -f%z "$icon_path" 2>/dev/null || stat -c%s "$icon_path" 2>/dev/null || echo "0")
            size_kb=$(echo "scale=1; $file_size / 1024" | bc 2>/dev/null || echo "?.?")
            total_size=$((total_size + file_size))
            echo "  ✅ $icon (${size_kb} KB) - expected: $expected_size"
        else
            echo "  ❌ $icon MISSING"
            all_exist=false
        fi
    done
done

echo ""
echo "===================================================="
total_kb=$(echo "scale=1; $total_size / 1024" | bc 2>/dev/null || echo "?.?")
echo "Total icons size: ${total_kb} KB"

if [ "$all_exist" = true ]; then
    echo "✅ All launcher icons are present!"
    exit 0
else
    echo "❌ Some icons are missing or have issues."
    echo ""
    echo "💡 To regenerate missing icons, run:"
    echo "   python generate_launcher_icons.py --output frontend_kotlin/app/src/main/res"
    exit 1
fi