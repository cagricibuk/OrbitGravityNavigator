import json
import math

def load_celestial_bodies(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {body['name']: body for body in data['celestialBodies']}

def parse_radius(radius_str):
    """Convert radius from string format (e.g. '600,000 m') to float in meters."""
    return float(radius_str.replace(',', '').replace(' m', ''))

def parse_orbital_period(orbital_period):
    """Convert orbital period from string format to seconds."""
    days, hours, minutes, seconds = map(float, orbital_period.replace('d', '').replace('h', '').replace('m', '').replace('s', '').split())
    total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
    return total_seconds

def calculate_transfer_time(start_body, end_body):
    # Başlangıç ve varış gök cisimlerinin verilerini al
    start_radius = parse_radius(start_body['radius'])  # m
    end_radius = parse_radius(end_body['radius'])      # m
    
    # Transfer süresini hesapla
    transfer_time = math.sqrt((start_radius**3 + end_radius**3) / (start_radius * end_radius))
    
    # Transfer süresini gün cinsine çevir
    transfer_days = transfer_time / 86400  # seconds to days
    return transfer_days

def main():
    print("Kerbal Space Program için Interplanetary Transfer Hesaplayıcı")
    
    celestial_bodies = load_celestial_bodies('data/celestialBodies.json')
    print("Mevcut Gezegenler:", ", ".join(celestial_bodies.keys()))

    start_body_name = input("Başlangıç gök cisimini girin: ")
    end_body_name = input("Varış gök cisimini girin: ")

    if start_body_name in celestial_bodies and end_body_name in celestial_bodies:
        start_body = celestial_bodies[start_body_name]
        end_body = celestial_bodies[end_body_name]
        
        transfer_time = calculate_transfer_time(start_body, end_body)
        print(f"{start_body_name} ile {end_body_name} arasında transfer süresi yaklaşık {transfer_time:.2f} gün.")
    else:
        print("Geçersiz gök cismi adı. Lütfen doğru bir gök cismi girin.")

if __name__ == "__main__":
    main()
