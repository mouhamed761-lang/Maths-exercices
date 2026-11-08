import streamlit as st

st.set_page_config(
    page_title="منسق سلاسل التمارين - الأستاذ عبد الله",
    page_icon="📐",
    layout="wide"
)

st.sidebar.header("⚙️ إعدادات الترويسة")
school_name = st.sidebar.selectbox("اختر المؤسسة التعليمية", ["lycée Akjoujt", "مدارس الفجر الحديثة", "مؤسسة أخرى"])
teacher_name = st.sidebar.text_input("اسم الأستاذ", value="Abdellahi Ahmedou")
academic_level = st.sidebar.selectbox("المستوى الدراسي", ["سنة أولى إعدادي / ثانوي (1AS)", "سنة ثانية (2AS)", "سنة ثالثة (3AS)", "باكالوريا - رياضيات / علوم (Série D)"])
subject = st.sidebar.text_input("المادة", value="الرياضيات")
academic_year = st.sidebar.text_input("السنة الدراسية", value="2026 - 2027")

st.title("📄 منشئ سلاسل التمارين الرياضية")
st.write("أداة مخصصة لترتيب الفروض وسلاسل التمارين بشكل رسمي واحترافي.")

col1, col2 = st.columns(2)
with col1:
    series_title = st.text_input("عنوان السلسلة", "سلسلة تمارين رقم 01")
with col2:
    unit_name = st.text_input("الوحدة أو المجال (اختياري)", "المجال: التحليل")

st.markdown("---")
st.subheader("✍️ إدخال التمارين")

if "exercises" not in st.session_state:
    st.session_state.exercises = ["التمرين الأول: \nنعتبر الدالة العددية المعرفة كما يلي..."]

if st.button("➕ إضافة تمرين جديد"):
    st.session_state.exercises.append(f"التمرين رقم {len(st.session_state.exercises) + 1}: \nنص التمرين هنا...")

updated_exercises = []
for i, ex in enumerate(st.session_state.exercises):
    col_del, col_text = st.columns([0.08, 0.92])
    with col_text:
        edited_ex = st.text_area(f"نص التمرين {i+1}", value=ex, height=120, key=f"ex_{i}")
        updated_exercises.append(edited_ex)
    with col_del:
        st.write("")
        st.write("")
        if st.button("🗑️", key=f"del_{i}"):
            st.session_state.exercises.pop(i)
            st.rerun()

st.session_state.exercises = updated_exercises
st.markdown("---")

st.subheader("👁️ معاينة ورقة التمرين النهائية")
exercises_html = ""
for i, ex in enumerate(st.session_state.exercises):
    formatted_ex = ex.replace('\n', '<br>')
    exercises_html += f"<div style='margin-bottom: 20px;'><strong>التمرين {i+1}:</strong><br>{formatted_ex}</div>"

printable_content = f"""
<div id='print-area' style="border: 2px solid #333; padding: 40px; border-radius: 8px; background-color: #ffffff; color: #000000; direction: rtl; font-family: Arial, sans-serif;">
    <table style="width: 100%; border: none; margin-bottom: 20px;">
        <tr>
            <td style="text-align: right; font-weight: bold; font-size: 14px;">
                الجمهورية الإسلامية الموريتانية<br>
                {school_name}<br>
                المادة: {subject}
            </td>
            <td style="text-align: left; font-weight: bold; font-size: 14px;">
                الأستاذ: {teacher_name}<br>
                المستوى: {academic_level}<br>
                السنة الدراسية: {academic_year}
            </td>
        </tr>
    </table>
    <hr style="border: 1px solid #333; margin-bottom: 20px;">
    <h2 style="text-align: center; color: #000000; margin-bottom: 5px;">{series_title}</h2>
    <p style="text-align: center; font-style: italic; color: #555; margin-bottom: 30px;">{unit_name}</p>
    <div style="font-size: 15px; line-height: 1.6;">
        {exercises_html}
    </div>
</div>
"""

st.markdown(printable_content, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🖨️ طباعة الورقة أو حفظها كملف PDF", type="primary"):
    st.markdown("<script>window.print();</script>", unsafe_allow_html=True)
    st.success("تم فتح نافذة الطباعة! يمكنك اختيار 'حفظ كـ PDF'.")
