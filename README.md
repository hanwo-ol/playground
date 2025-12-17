# U-Net Review Blog 🧬

U-Net 기반 모델 논문을 자동으로 수집하고 리뷰할 수 있는 블로그 프로젝트입니다. Hugo(PaperMod 테마)를 기반으로 구축되었으며, ArXiv에서 최신 논문을 가져오는 Python 스크립트가 포함되어 있습니다.

## 🚀 시작하기 (Getting Started)

로컬 컴퓨터에서 이 블로그를 실행하고 관리하는 방법입니다.

### 1. 필수 도구 설치

이 프로젝트를 실행하려면 **Git**, **Python**, **Hugo**가 필요합니다.

*   **Git:** [설치 가이드](https://git-scm.com/downloads)
*   **Python (3.8+):** [설치 가이드](https://www.python.org/downloads/)
*   **Hugo (Extended 버전 필수):**
    *   **Windows:** [Chocolatey](https://chocolatey.org/) 사용 권장 (`choco install hugo-extended`) 또는 [릴리즈 페이지](https://github.com/gohugoio/hugo/releases)에서 `hugo_extended_..._windows-amd64.zip` 다운로드 후 PATH 설정.
    *   **Mac:** `brew install hugo`
    *   **Linux:** [릴리즈 페이지](https://github.com/gohugoio/hugo/releases)에서 `hugo_extended_..._linux-amd64.deb` 다운로드 후 설치.

### 2. 프로젝트 클론 및 설정

터미널(또는 명령 프롬프트)을 열고 다음 명령어를 입력합니다.

```bash
# 저장소 클론 (본인의 저장소 주소로 변경)
git clone https://github.com/hanwo-ol/playground.git
cd playground

# Python 의존성 설치 (논문 수집 스크립트용)
pip install -r requirements.txt
```

### 3. 블로그 로컬 실행 (미리보기)

내 컴퓨터에서 블로그 화면을 확인하려면 다음 명령어를 실행합니다.

```bash
hugo server -D
```

*   `-D` 옵션은 `draft: true` (작성 중) 상태인 글도 보여줍니다.
*   브라우저에서 `http://localhost:1313`으로 접속하면 블로그를 볼 수 있습니다.

---

## 🤖 논문 자동 수집 (Automation)

`fetch_papers.py` 스크립트를 실행하면 ArXiv에서 새로운 U-Net 관련 논문을 가져와 포스트 초안을 생성합니다.

### 실행 방법

```bash
python fetch_papers.py
```

*   실행 시 최신 논문 10개를 가져옵니다.
*   이미 가져온 논문은 `history.json`에 기록되어 중복으로 가져오지 않습니다.
*   생성된 파일은 `content/posts/` 폴더에 저장됩니다.

### 🔍 검색 쿼리 수정하기 (Customizing Search)

`fetch_papers.py` 파일을 열어 상단의 `QUERY` 변수를 수정하면 검색 조건을 변경할 수 있습니다.

**현재 설정:**
```python
# U-Net, UNet, segmentation 중 하나라도 포함된 논문 검색
QUERY = 'all:%22U-Net%22+OR+all:%22UNet%22+OR+all:%22segmentation%22'
```

**수정 방법 (ArXiv API 문법):**
*   `all:` : 제목, 초록, 저자 등 전체 검색
*   `ti:` : 제목(Title)만 검색
*   `abs:` : 초록(Abstract)만 검색
*   `AND`, `OR`, `ANDNOT` 연산자 사용 가능
*   공백은 `+`로, 따옴표는 `%22`로 표기해야 안전합니다.

**예시:**
1.  **"Medical"이 포함된 U-Net 논문만 찾고 싶을 때:**
    ```python
    # (U-Net OR UNet) AND Medical
    QUERY = '(all:%22U-Net%22+OR+all:%22UNet%22)+AND+all:%22Medical%22'
    ```
2.  **제목에 "Attention"이 들어간 논문 찾기:**
    ```python
    QUERY = 'ti:%22Attention%22+AND+(all:%22U-Net%22+OR+all:%22UNet%22)'
    ```

---

## 🌍 배포하기 (Deployment)

이 블로그는 GitHub Pages를 통해 배포됩니다. 로컬에서 글을 다 쓴 후 배포하려면 다음 과정을 따르세요.

1.  **빌드 스크립트 실행:**
    ```bash
    ./build.sh
    # 윈도우에서는 Git Bash를 사용하거나 'hugo --destination docs' 명령어를 직접 입력하세요.
    ```
    이 명령은 `docs/` 폴더에 최종 웹사이트 파일들을 생성합니다.

2.  **GitHub에 업로드:**
    ```bash
    git add .
    git commit -m "새 논문 리뷰 추가"
    git push origin main
    ```

3.  **배포 확인:**
    *   잠시 후 `https://hanwo-ol.github.io/playground/` 에서 변경 사항을 확인할 수 있습니다.
    *   (최초 설정 시) GitHub 저장소 Settings > Pages에서 Source를 `Deploy from a branch`, Branch를 `main`, Folder를 `/docs`로 설정해야 합니다.

## 📝 글 작성 가이드

*   자동 생성된 파일(`content/posts/*.md`)을 열어 내용을 수정하세요.
*   `draft: true`를 `draft: false`로 변경하면 정식으로 공개됩니다 (로컬 서버에서 `-D` 없이도 보임).
*   `## ✍️ Review` 섹션에 본인의 리뷰를 작성하면 됩니다. 수식은 `$E=mc^2$` 처럼 달러 기호를 사용하여 작성할 수 있습니다.
