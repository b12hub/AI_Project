# run.py
# Barcha jarayonni ishga tushirish

from data_collector import TransportDataCollector
import time

def main():
    print("""
    ╔════════════════════════════════════════════════════╗
    ║   TRANSPORT & LOGISTICS DATA COLLECTOR             ║
    ║   60,000+ qator malumot yig'ish                    ║
    ╚════════════════════════════════════════════════════╝
    """)
    
    start_time = time.time()
    
    # Collector yaratish
    collector = TransportDataCollector()
    
    # Data yig'ish
    try:
        data = collector.generate_dataset(target_rows=70000)
        
        # CSV ga saqlash
        df = collector.save_to_csv()
        
        # Statistika
        elapsed_time = time.time() - start_time
        
        print("\n" + "=" * 60)
        print("✅ MUVAFFAQIYATLI YAKUNLANDI!")
        print("=" * 60)
        print(f"⏱  Vaqt: {elapsed_time:.1f} soniya")
        print(f"📊 Qatorlar: {len(df)}")
        print(f"📁 Fayl: output/raw_data.csv")
        print("\n💡 Keyingi qadam: Data cleaning va EDA")
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Jarayon to'xtatildi (Ctrl+C)")
        
    except Exception as e:
        print(f"\n\n❌ XATOLIK: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()