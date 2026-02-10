import os
import django
from django.utils import timezone
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trekking_project.settings')
django.setup()

from django.contrib.auth.models import User
from articles.models import BaiHuongDan, ChuyenMuc

def create_articles():
    print("--- Starting Knowledge Data Generation ---")

    # 1. Ensure Categories
    categories = [
        "Kỹ năng sinh tồn",
        "Chuẩn bị & Lên kế hoạch",
        "Sơ cứu y tế",
        "Ẩm thực dã ngoại",
        "Review Gear & Dụng cụ"
    ]
    
    cat_objs = {}
    for cat_name in categories:
        cat, created = ChuyenMuc.objects.get_or_create(ten=cat_name)
        cat_objs[cat_name] = cat
        if created:
            print(f"Created category: {cat_name}")

    # 2. Get Authors (Admins or reliable users)
    authors = list(User.objects.filter(is_staff=True))
    if not authors:
        authors = list(User.objects.all())
    
    if not authors:
        print("No users found to set as authors.")
        return

    # 3. Define Articles
    articles_data = [
        {
            "title": "5 Kỹ năng sinh tồn cơ bản khi lạc trong rừng",
            "cat": "Kỹ năng sinh tồn",
            "content": """
            <p>Lạc trong rừng là nỗi ác mộng của bất kỳ trekker nào. Tuy nhiên, nếu nắm vững 5 kỹ năng sau, cơ hội sống sót của bạn sẽ tăng lên đáng kể.</p>
            <h3>1. Giữ bình tĩnh (S.T.O.P)</h3>
            <p>Nguyên tắc S.T.O.P: Sit (Ngồi xuống), Think (Suy nghĩ), Observe (Quan sát), Plan (Lên kế hoạch). Đừng hoảng loạn chạy lung tung.</p>
            <h3>2. Tìm nguồn nước</h3>
            <p>Cơ thể con người chỉ chịu được 3 ngày không nước. Hãy tìm suối, rễ cây ngậm nước hoặc hứng sương đêm.</p>
            <h3>3. Tạo lửa</h3>
            <p>Lửa giúp giữ ấm, nấu chín thức ăn, đuổi thú dữ và phát tín hiệu cầu cứu. Luôn mang theo bật lửa hoặc đá đánh lửa.</p>
            <h3>4. Dựng lều trú ẩn</h3>
            <p>Một chỗ trú ẩn an toàn tránh mưa gió và côn trùng là vô cùng quan trọng khi màn đêm buông xuống.</p>
            <h3>5. Phát tín hiệu</h3>
            <p>Sử dụng khói, gương phản chiếu, hoặc xếp đá hình chữ SOS ở nơi thoáng đãng.</p>
            """
        },
        {
            "title": "Checklist đồ dùng cần thiết cho chuyến trekking 2 ngày 1 đêm",
            "cat": "Chuẩn bị & Lên kế hoạch",
            "content": """
            <p>Chuẩn bị kỹ lưỡng là chìa khóa cho một chuyến đi thành công. Dưới đây là danh sách những vật dụng "bất ly thân".</p>
            <ul>
                <li><strong>Balo:</strong> Loại có trợ lực, dung tích 40-50L.</li>
                <li><strong>Giày trekking:</strong> Đế gai bám tốt, chống thấm nước.</li>
                <li><strong>Trang phục:</strong> Quần áo mau khô, áo khoác gió, áo giữ nhiệt.</li>
                <li><strong>Đồ ngủ:</strong> Túi ngủ phù hợp nhiệt độ, lều hoặc võng.</li>
                <li><strong>Y tế:</strong> Bông băng, thuốc sát trùng, thuốc tiêu hóa, hạ sốt.</li>
                <li><strong>Đèn pin:</strong> Đèn đội đầu để rảnh tay di chuyển.</li>
            </ul>
            """
        },
        {
            "title": "Sơ cứu khi bị rắn cắn: Những sai lầm cần tránh",
            "cat": "Sơ cứu y tế",
            "content": """
            <p>Rắn độc là mối nguy hiểm tiềm tàng. Xử lý sai cách có thể khiến nọc độc lan nhanh hơn.</p>
            <h3>KHÔNG làm những việc sau:</h3>
            <ul>
                <li>Không garo quá chặt làm hoại tử chi.</li>
                <li>Không rạch vết thương để hút nọc độc.</li>
                <li>Không đắp lá thuốc không rõ nguồn gốc.</li>
            </ul>
            <h3>Nên làm:</h3>
            <p>Rửa sạch vết thương bằng nước muối sinh lý, băng ép nhẹ, hạn chế vận động và chuyển nạn nhân đến cơ sở y tế gần nhất.</p>
            """
        },
        {
            "title": "Bí quyết nấu cơm lam thơm dẻo giữa rừng",
            "cat": "Ẩm thực dã ngoại",
            "content": """
            <p>Cơm lam là món ăn đặc sản của núi rừng. Để nấu ngon, bạn cần chọn ống nứa tươi, gạo nếp nương dẻo thơm.</p>
            <p>Ngâm gạo trước 4-6 tiếng. Cho gạo vào ống nứa, đổ nước xăm xắp, nút lá chuối lại. Nướng trên than hồng, xoay đều tay cho đến khi nứa cháy xém và có mùi thơm lừng bốc lên.</p>
            """
        },
        {
            "title": "Review Giày Trekking The North Face: Đáng tiền hay không?",
            "cat": "Review Gear & Dụng cụ",
            "content": """
            <p>Sau 5 chuyến đi Tả Liên Sơn, mình có vài đánh giá về đôi giày này.</p>
            <p><strong>Ưu điểm:</strong> Chống nước Gore-tex cực tốt, đế Vibram bám đá chắc chắn, form ôm chân thoải mái.</p>
            <p><strong>Nhược điểm:</strong> Giá thành hơi cao, cần break-in (đi mềm) trước khi đi xa.</p>
            <p><strong>Kết luận:</strong> Rất đáng đầu tư cho những ai đam mê trekking lâu dài.</p>
            """
        },
         {
            "title": "Cách đọc bản đồ địa hình và sử dụng la bàn",
            "cat": "Kỹ năng sinh tồn",
            "content": """
            <p>Trong thời đại GPS, kỹ năng đọc bản đồ giấy vẫn cực kỳ quan trọng khi thiết bị điện tử hết pin.</p>
            <p>Hiểu về đường đồng mức: Các đường càng sát nhau thì dốc càng đứng. Vùng thưa đường là địa hình bằng phẳng.</p>
            <p>Định hướng bản đồ về hướng Bắc bằng la bàn trước khi xác định vị trí.</p>
            """
        },
    ]

    # 4. Loop Create
    for data in articles_data:
        # Check duplicate title
        if BaiHuongDan.objects.filter(tieu_de=data['title']).exists():
            print(f"Article '{data['title']}' already exists. Skipping.")
            continue

        cat = cat_objs.get(data['cat'])
        author = random.choice(authors)
        
        BaiHuongDan.objects.create(
            tieu_de=data['title'],
            chuyen_muc=cat,
            noi_dung=data['content'],
            tac_gia=author,
            da_duyet=True, # Auto approve
            nguoi_duyet=authors[0] if authors[0].is_staff else None,
            ngay_duyet=timezone.now()
        )
        print(f"Created article: {data['title']} (Cat: {data['cat']})")

    print("--- Finished ---")

if __name__ == "__main__":
    create_articles()
